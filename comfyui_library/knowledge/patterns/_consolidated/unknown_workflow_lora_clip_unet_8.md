---
name: unknown_workflow_lora_clip_unet_8
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.854833
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, ImageScaleToTotalPixels, ImageSharpen, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, workflow>自定义采样器]
problems: []
missing: []
members: [图片生成/图生图/Zimage-Klein高清洗图双采样放大_2058022601766821890.json, 图片生成/图生图/高清洗图Zimage双采样Klein放大_2048324311714369537.json, 图片生成/文生图/Zimage+生图+洗图+双采样+Klein放大_2070378304154193922.json, 图片生成/文生图/最新全能模型G-image2_4K放大版_极速生图_图像编辑_2046761253904846850.json, 图片生成/文生图/生图_洗图_Zimage双采样+Klein放大_2020509073417969666.json, 图片生成/文生图/高清洗图Zimage双采样放大Klein_2050607497655926786.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Zimage-Klein高清洗图双采样放大_2058022601766821890.json、图片生成/图生图/高清洗图Zimage双采样Klein放大_2048324311714369537.json、图片生成/文生图/Zimage+生图+洗图+双采样+Klein放大_2070378304154193922.json、图片生成/文生图/最新全能模型G-image2_4K放大版_极速生图_图像编辑_2046761253904846850.json、图片生成/文生图/生图_洗图_Zimage双采样+Klein放大_2020509073417969666.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `workflow>自定义采样器`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 5/6 个有
- `KSamplerAdvanced` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `easy clearCacheAll` —— 5/6 个有
- `workflow>LLama-ccp提示词反推` —— 5/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `TextInput_` —— 2/6 个有
- `CR Image Input Switch` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `RH_RhartImageG2ImageToImage` —— 1/6 个有
- `RH_RhartImageG2TextToImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | res_multistep | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
