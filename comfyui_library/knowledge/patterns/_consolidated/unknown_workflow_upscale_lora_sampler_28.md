---
name: unknown_workflow_upscale_lora_sampler_28
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.902286
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, ImageSharpen, KSamplerAdvanced, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/文生图图像生成器_2036011868971601922.json, 图片生成/文生图/最新版万能图像生成器-太牛逼了_2028849021414023170.json, 图片生成/文生图/自用-万能图像生成器工作流_2037031301642981378.json, 图片生成/文生图/角色设计（动漫）-橘_2053012314667925506.json, 图片生成/文生图/超强自定义角色生成_2024732759662530561.json, 图片生成/文生图/超级双采8k 出图_2073110455563939841.json, 图片生成/文生图/👾怪獸-国风角色设计👾_2058099509644840962.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/文生图图像生成器_2036011868971601922.json、图片生成/文生图/最新版万能图像生成器-太牛逼了_2028849021414023170.json、图片生成/文生图/自用-万能图像生成器工作流_2037031301642981378.json、图片生成/文生图/角色设计（动漫）-橘_2053012314667925506.json、图片生成/文生图/超强自定义角色生成_2024732759662530561.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `Int` —— 5/7 个有
- `Label (rgthree)` —— 4/7 个有
- `CLIPLoaderGGUF` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `ProcessString` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `easy promptLine` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `AILab_QwenVL` —— 1/7 个有
- `DuckHideNode` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `StringReplace` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 7 | 98% |
| 高度 | 1536 | 1536 - 1920 | 7 | 92% |
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 7 | 100% |
| 采样算法 | 1 | 1 - 2 | 7 | 65% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，7 个样本，取值集中（一致性 98%）
- 高度 中位数 1536，观测区间 1536 - 1920，7 个样本，取值集中（一致性 92%）
- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 2，7 个样本
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
