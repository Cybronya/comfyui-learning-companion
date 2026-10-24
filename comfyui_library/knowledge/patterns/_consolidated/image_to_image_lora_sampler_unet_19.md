---
name: image_to_image_lora_sampler_unet_19
type: Image To Image
frequency: 18
level: strong
coverage: 0.935278
common_nodes: [CLIPLoader, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 扩图工作流（自定义尺寸快速扩图）_2078108311949496321.json, 图片生成/图生图/Krea2 扩图（自定义尺寸快速扩图）_2078375469275238402.json, 图片生成/图生图/Krea2-Edit 单图编辑_2075230413626368001.json, 图片生成/图生图/Krea2-edit-万物移除工作流_2083364214013513730.json, 图片生成/图生图/Krea2-edit-局部重绘_2081180832265494529.json, 图片生成/图生图/Krea2-edit-局部重绘_2100068626303901698.json, 图片生成/图生图/Krea2-edit-局部重绘_2100145240756801538.json, 图片生成/图生图/Krea2-扩图工作流_2079205072847851521.json, 图片生成/图生图/Krea2-扩图工作流_2081308936606666754.json, 图片生成/图生图/Krea2_8步扩图_自定义尺寸_2079334798514024449.json, 图片生成/图生图/Krea2_8步扩图_自定义尺寸_2080937877667672066.json, 图片生成/图生图/Krea2_扩图工作流自定义尺寸快速扩图_2079020454119043073.json, 图片生成/图生图/Krea2_扩图工作流自定义尺寸快速扩图_2079402657093079041.json, 图片生成/图生图/krea2-edit-1.2-单图编辑_2080188714176827393.json, 图片生成/图生图/krea2-edit-换脸换头_2081729309529694210.json, 图片生成/图生图/krea2-edit-换装（服装迁移）_2081734940332478465.json, 图片生成/图生图/krea2-edit-角色多视角生成_2081725516587032578.json, 图片生成/图生图/krea2-角色四视图生成_2095481547678904322.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_19

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Krea2 扩图工作流（自定义尺寸快速扩图）_2078108311949496321.json、图片生成/图生图/Krea2 扩图（自定义尺寸快速扩图）_2078375469275238402.json、图片生成/图生图/Krea2-Edit 单图编辑_2075230413626368001.json、图片生成/图生图/Krea2-edit-万物移除工作流_2083364214013513730.json、图片生成/图生图/Krea2-edit-局部重绘_2081180832265494529.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 17/18 个有
- `CR Prompt Text` —— 15/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/18 个有
- `DrawMaskOnImage` —— 12/18 个有
- `ConditioningZeroOut` —— 11/18 个有
- `ImagePadForOutpaint` —— 8/18 个有
- `easy int` —— 8/18 个有
- `Int` —— 4/18 个有
- `Mask Fill Holes` —— 4/18 个有
- `ImageColorMatchAdobe+` —— 3/18 个有
- `kkPadImageToCanvas` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | beta | - | 18 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
