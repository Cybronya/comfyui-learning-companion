# BNK_CLIPTextEncodeAdvanced

## 节点类型

`BNK_CLIPTextEncodeAdvanced`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（6 次）

## 输出

- `CONDITIONING:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["over sharpening,dirt,bad color matching,graying,wrong perspective,distorted person,Twisted Car,NSFW,worst quality,low `（3 次）
- `["mir,sunnyday,sunlight,modern architectures,a skyscraper building in the center of the picture,cityscape,intersection,c`（1 次）
- `["mir,he image features courtyard architecture,characterized by white walls,two slope roof,with an open pathway flanked `（1 次）
- `["zwzt,jzcgxl001,aerial view of a bustling city,river,golden lighting,blue hour,city park,night,", "length+mean", "A1111`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
