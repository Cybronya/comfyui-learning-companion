# RunningHub Void Point Editor

## 节点类型

`RunningHub Void Point Editor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `preview_stride:INT`（3 次）
- `upload:STRING`（3 次）
- `upload_status:STRING`（3 次）
- `points_store:STRING`（3 次）
- `coordinates:STRING`（3 次）

## 输出

- `video:VIDEO`（3 次）
- `primary_points_by_frame:RHVoidPoints`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, "da3e666e64d2789e62540d4804ce6c4536013be28f77637ac36abcbb9411f4cd.mp4", "success", "{\"0\":[[223,104],[281,62],[271,`（1 次）
- `[4, "da4a71b07e784d2cbaff1cb8d5082babc9e910ff23e943c3e9db689397698227.mp4", "success", "{\"0\":[[255,1377],[409,1365],[5`（1 次）
- `[4, "dee7043f250ca22819b35b701ad5998841d90cc57f23eb85b37b2fd2b0645d4a.mp4", "success", "{\"0\":[[91,513],[22,642],[132,7`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
