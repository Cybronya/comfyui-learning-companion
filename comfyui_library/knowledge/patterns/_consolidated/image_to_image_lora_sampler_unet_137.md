---
name: image_to_image_lora_sampler_unet_137
type: Image To Image
frequency: 5
level: strong
coverage: 0.693
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/千问多角度图像编辑_2050499840190234626.json, 图片生成/文生图/可视化精准定义角度和距离镜头+全节点注释_2055985534916415489.json, 图片生成/文生图/手动改变图片角度和镜头=Multiple2511_2009946377266143234.json, 图片生成/文生图/生成角色三视图 手动自由切换俯仰_推拉视角+全节点注释_2084842862851747842.json, 图片生成/文生图/生成角色三视图 手动自由切换俯仰_推拉视角+全节点注释_2085222342405484546.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_137

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/千问多角度图像编辑_2050499840190234626.json、图片生成/文生图/可视化精准定义角度和距离镜头+全节点注释_2055985534916415489.json、图片生成/文生图/手动改变图片角度和镜头=Multiple2511_2009946377266143234.json、图片生成/文生图/生成角色三视图 手动自由切换俯仰_推拉视角+全节点注释_2084842862851747842.json、图片生成/文生图/生成角色三视图 手动自由切换俯仰_推拉视角+全节点注释_2085222342405484546.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 4/5 个有
- `VNCCS_VisualPositionControl` —— 4/5 个有
- `easy promptList` —— 4/5 个有
- `QwenMultiangleCameraNode` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `KepStringLiteral` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `VAEDecodeTiled` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 5 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，5 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
