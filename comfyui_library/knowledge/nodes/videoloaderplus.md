# VideoLoaderPlus

## 节点类型

`VideoLoaderPlus`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `file:COMBO`（2 次）
- `upload:IMAGEUPLOAD`（2 次）

## 输出

- `VIDEO:VIDEO`（2 次）
- `PATH:PATH`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["b00f3de6dfada9128bd1964c25f9083a86f32074f4fc2baee79ca848a64a8973.mp4", "image"]`（1 次）
- `["9054755787fba5cb252a162743f29984e3ee1ac019d05ea4f441a958c2384211.mp4", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
