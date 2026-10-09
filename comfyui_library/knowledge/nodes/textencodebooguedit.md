# TextEncodeBooguEdit

## 节点类型

`TextEncodeBooguEdit`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `images.image_1:IMAGE`（1 次）
- `images.image_2:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["opticscene, 将输入的蔡司眼镜白底产品图转换为专业光学生活方式场景图。严格保持原眼镜的镜框轮廓、镜片形状、鼻梁、镜腿、材质、颜色、比例和品牌细节不变；仅增加真实自然的使用场景、人物佩戴关系、光影、空间与氛围。眼镜必须清晰可辨、`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
