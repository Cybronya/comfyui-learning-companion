---
name: text_to_image_lora_sampler_clip_268
type: Text To Image
frequency: 7
level: strong
coverage: 0.863143
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, ResizeImageMaskNode, ResolutionSelector, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2+SeedVR2_2100855495958548481.json, 图片生成/文生图/Krea2巨构+SeedVR2放大_2093260084464934914.json, 图片生成/文生图/Krea2巨构+SeedVR2放大_2100477000350781442.json, 图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2083394345272692737.json, 图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2095744406384103426.json, 图片生成/文生图/南音创作，大尺☠️-只有你想不到的_2092714226971406337.json, 图片生成/文生图/文生图超写实krea2+SeedVR放大_2089957625613082626.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_268

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Krea2+SeedVR2_2100855495958548481.json、图片生成/文生图/Krea2巨构+SeedVR2放大_2093260084464934914.json、图片生成/文生图/Krea2巨构+SeedVR2放大_2100477000350781442.json、图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2083394345272692737.json、图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2095744406384103426.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `Any Switch (rgthree)` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `FlashVSRNode` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |
| 采样步数 | 8 | 8 - 10 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 10，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
