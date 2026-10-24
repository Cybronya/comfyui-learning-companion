# DapaoImageMultiSwitchNode

## 节点类型

`DapaoImageMultiSwitchNode`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `🎯 编号:INT`（4 次）
- `⏭️ 跳过空图片:BOOLEAN`（4 次）
- `🔄 循环模式:BOOLEAN`（4 次）
- `image3:IMAGE`（3 次）
- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image4:IMAGE`（2 次）
- `image5:IMAGE`（2 次）
- `image6:IMAGE`（1 次）
- `image8:IMAGE`（1 次）

## 输出

- `🖼️ 图像:IMAGE`（4 次）
- `ℹ️ 信息:STRING`（4 次）
- `🔢 索引:INT`（4 次）
- `📊 总数:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, true, true]`（3 次）
- `[1, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
