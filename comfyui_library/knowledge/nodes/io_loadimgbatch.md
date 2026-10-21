# IO_LoadImgBatch

## 节点类型

`IO_LoadImgBatch`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image_list_in:IMAGE`（2 次）
- `image_list:STRING`（2 次）
- `card_size:INT`（2 次）
- `index:INT`（2 次）

## 输出

- `img_list:IMAGE`（2 次）
- `img_index:IMAGE`（2 次）
- `name_index:STRING`（2 次）
- `index:INT`（2 次）
- `total:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["63fd88ddc39269ad7a289e192953e39a7367bd8047a19f471cfe3659fa34924d.jpg\ned3e2fbb3c89009b0ff537ae3519614b29831ae0e37e7b87`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
