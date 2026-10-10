# RH_ViduQ3_Text2Video

## 节点类型

`RH_ViduQ3_Text2Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）
- `style:COMBO`（2 次）
- `aspect_ratio:COMBO`（2 次）
- `resolution:COMBO`（2 次）
- `duration:COMBO`（2 次）
- `audio:BOOLEAN`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["宏大的科幻大片视角，大型伸缩炮（Technocrane）机械臂运镜。镜头在巨大的空间站内部进行 360 度弧形横扫，随后平滑推进。画面充满体积光（光）和漂浮的微尘。极致的细节刻画，IMAX 银幕比例，充满张力的构图，仿佛置身于未来史诗电`（1 次）
- `["16:9，4K超高清，电影级运镜，中式古代海上海战场景，**无现代元素**，天光暗沉的黄昏，海面翻涌暗蓝巨浪，整体色调苍劲沉郁（古铜+焦黑+暗蓝主调），画面带轻微电影颗粒感，氛围感拉满\n0-2秒：高空全景俯冲，展现海面帆樯林立，数十艘`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
