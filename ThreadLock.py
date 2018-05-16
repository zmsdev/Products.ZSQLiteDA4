def allocate_lock():
  lock = DummyThreadLock()
  print("Products.ZSQLiteDA.ThreadLock::allocation_lock",lock)
  return lock
class DummyThreadLock:
  def acquire(self):
    print("Products.ZSQLiteDA.ThreadLock::DummyThreadLock.acquire")
  def release(self):
    print("Products.ZSQLiteDA.ThreadLock::DummyThreadLock.release")