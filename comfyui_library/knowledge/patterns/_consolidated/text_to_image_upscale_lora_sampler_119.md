---
name: text_to_image_upscale_lora_sampler_119
type: Text To Image
frequency: 2
level: weak
coverage: 0.5855
common_nodes: [AILab_MaskExtractor, Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, Image Comparer (rgthree), KSampler, LoadAndResizeImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, ResizeImageMaskNode, SAM3_Detect, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SetNode, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1换脸换头换人精准万物迁移工作流，SAM3遮罩编辑方案_2105755857714769921.json, 平台全量/3-效果炸裂 合规使用！QwenImage2.1换脸换头换人 精准万物迁移工作流-V1_2105196366719963137.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_119

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1换脸换头换人精准万物迁移工作流，SAM3遮罩编辑方案_2105755857714769921.json、平台全量/3-效果炸裂 合规使用！QwenImage2.1换脸换头换人 精准万物迁移工作流-V1_2105196366719963137.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_MaskExtractor`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadAndResizeImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResizeImageMaskNode`
- `SAM3_Detect`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SetNode`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1000 | - | 2 | 8% |
| 高度 | 584 | - | 2 | 14% |
| 采样步数 | 2.5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1000，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 高度 中位数 584，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
