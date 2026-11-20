---
name: image_to_image_lora_sampler_unet_193
type: Image To Image
frequency: 4
level: strong
coverage: 0.82125
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/老照片修复_2008934700944986113.json, 图片生成/图生图/老照片修复_2009751417199796225.json, 平台全量/Qwen-Edit-2511：多景别镜头，人物一致性_2030596127564767233.json, 平台全量/一键生成超稳定质感形象照_2038933460634570754.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_193

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/老照片修复_2008934700944986113.json、图片生成/图生图/老照片修复_2009751417199796225.json、平台全量/Qwen-Edit-2511：多景别镜头，人物一致性_2030596127564767233.json、平台全量/一键生成超稳定质感形象照_2038933460634570754.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `MemoryCleaner` —— 2/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `easy promptLine` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
