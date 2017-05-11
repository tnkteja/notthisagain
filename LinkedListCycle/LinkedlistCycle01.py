def has_cycle(head):
    slowref=head
    if not slowref or not slowref.next:
        return False
    fastref=head.next.next
    while slowref != fastref:
        slowref=slowref.next
        if not slowref or not slowref.next:
            return False
        fastref=fastref.next.next
    return True