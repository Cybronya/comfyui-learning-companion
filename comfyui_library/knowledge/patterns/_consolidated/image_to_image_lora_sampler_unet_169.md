---
name: image_to_image_lora_sampler_unet_169
type: Image To Image
frequency: 4
level: strong
coverage: 0.77575
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/老照片修复_2008934700944986113.json, 图片生成/图生图/老照片修复_2009751417199796225.json, 图片生成/图生图/通义Qwen2511 多角度视角自由切换_2015670502123118594.json, 图片生成/图生图/😶‍🌫️千问2511 多角度自由切换🐳_2009500325392158722.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_169

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/老照片修复_2008934700944986113.json、图片生成/图生图/老照片修复_2009751417199796225.json、图片生成/图生图/通义Qwen2511 多角度视角自由切换_2015670502123118594.json、图片生成/图生图/😶‍🌫️千问2511 多角度自由切换🐳_2009500325392158722.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `MemoryCleaner` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `QwenMultiangleCameraNode` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `FluxKontextImageScale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
