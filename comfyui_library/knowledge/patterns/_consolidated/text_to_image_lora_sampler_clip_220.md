---
name: text_to_image_lora_sampler_clip_220
type: Text To Image
frequency: 9
level: moderate
coverage: 0.869778
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, ResizeImageMaskNode, ResolutionSelector, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2+SeedVR2_2100855495958548481.json, 图片生成/文生图/Krea2巨构+SeedVR2放大_2093260084464934914.json, 图片生成/文生图/Krea2巨构+SeedVR2放大_2100477000350781442.json, 图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2083394345272692737.json, 图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2095744406384103426.json, 图片生成/文生图/南音创作，大尺☠️-只有你想不到的_2092714226971406337.json, 图片生成/文生图/巨构图+SeedVR2放大｜Krea2文生图高清处理_2093743192297533442.json, 图片生成/文生图/巨物场景文生图｜Krea2生成+SeedVR2高清放大_2093417313402970114.json, 图片生成/文生图/文生图超写实krea2+SeedVR放大_2089957625613082626.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_220

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Krea2+SeedVR2_2100855495958548481.json、图片生成/文生图/Krea2巨构+SeedVR2放大_2093260084464934914.json、图片生成/文生图/Krea2巨构+SeedVR2放大_2100477000350781442.json、图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2083394345272692737.json、图片生成/文生图/krea2随手拍写实风文生图+官方版SeedVR放大_2095744406384103426.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ShowText|pysssss` —— 5/9 个有
- `ConditioningKrea2Rebalance` —— 4/9 个有
- `GetNode` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `Any Switch (rgthree)` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `JjkText` —— 2/9 个有
- `solarL_SaveImagesToZip` —— 2/9 个有
- `孤海注释` —— 2/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/9 个有
- `FlashVSRNode` —— 1/9 个有
- `GIMMVFI_interpolate` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 9 | 57% |
| 高度 | 512 | 80 - 512 | 9 | 57% |
| 采样步数 | 8 | 4 - 10 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 18% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | beta | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，9 个样本
- 高度 中位数 512，观测区间 80 - 512，9 个样本
- 采样步数 中位数 8，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 beta，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（15/9 个样本）：Steps较低可能导致细节不足
