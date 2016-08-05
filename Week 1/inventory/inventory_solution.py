"""
Inventory
---------

Calculate and report the current inventory in a warehouse.

Assume the warehouse is initially empty.

The string, warehouse_log, is a stream of deliveries to 
and shipments from a warehouse.  Each line represents
a single transaction for a part with the number of
parts delivered or shipped.  It has the form::

    part_id count

If "count" is positive, then it is a delivery to the
warehouse. If it is negative, it is a shipment from
the warehouse.

Use the functions provided in your solution, where process_log
parses the warehouse log string, and produces a list of
transactions, and process_transactions generates an inventory
dict from a list of transactions.  The function generate_inventory
calls process_log, then process_transactions.
"""

def process_log(log):
    """ Process a warehouse log string containing part names and counts.
    Return an iterator for a list of transactions.
    """
    return (line.strip().rsplit(None,1) for line in log.strip().split('\n'))
    #ALTERNATE SOLUTION:
    #import itertools
    #items = log.split()
    #return itertools.izip(items[::2],items[1::2])


def process_transactions(transactions, inventory={}):
    """Given a list of transactions and optionally an initial inventory,
    compute and return the final inventory for each part.
    """
    for part, count in transactions:
        inventory[part] = inventory.get(part, 0) + int(count)
    return inventory


def generate_inventory(log):
    """ Process a warehouse log string containing part names and counts.
    Returns a dict with the inventory of each part.
    """
    return process_transactions(process_log(log))


if __name__ == '__main__':

    warehouse_log = """ lightcycle       10
                        hoverboard        5
                        lightsaber       12
                        lightcycle       -3
                        lightcycle       20
                        phaser           40
                        hoverboard       -4
                        lightsaber       -8
                    """

    for part, count in generate_inventory(warehouse_log).iteritems():
        print '{0:>20s}: {1:>5d}'.format(part, count)


