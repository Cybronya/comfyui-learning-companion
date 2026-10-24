# AFL:QwenEditPlusFastuseV2

## 节点类型

`AFL:QwenEditPlusFastuseV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `vae:VAE`（3 次）
- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `images_vl1:COMBO`（3 次）
- `ref_latents1:COMBO`（3 次）
- `images_vl2:COMBO`（3 次）
- `ref_latents2:COMBO`（3 次）

## 输出

- `conditioning:CONDITIONING`（3 次）
- `con_zero_out:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["通用静物摄影，提升光照一致性，添加真实阴影效果（匹配光源），透明材质，光线折射与透射，细腻透明高光，实现主体与背景无缝融合，保留原始亮度，呈现自然且照片级真实感，无瑕疵,pysj", "NaN", "NaN", "ini(384x384`（1 次）
- `["切换角色动作，姿势参考图二", "ini(384x384)", "ini(1024*1024)", "ini(384x384)", "ini(1024*1024)", "ini(384x384)", "ini(1024*1024)", `（1 次）
- `["给图1的人物穿上图2的衣服，保持人物一致性", "ini(384x384)", "NaN", "ini(384x384)", "NaN", "ini(384x384)", "ini(1024*1024)", "image1"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
