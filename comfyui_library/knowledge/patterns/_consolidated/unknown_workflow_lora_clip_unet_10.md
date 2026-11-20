---
name: unknown_workflow_lora_clip_unet_10
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.855571
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, ImageScaleToTotalPixels, ImageSharpen, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, workflow>自定义采样器]
problems: []
missing: []
members: [图片生成/图生图/Zimage-Klein高清洗图双采样放大_2058022601766821890.json, 图片生成/图生图/高清洗图Zimage双采样Klein放大_2048324311714369537.json, 图片生成/文生图/Zimage+生图+洗图+双采样+Klein放大_2070378304154193922.json, 图片生成/文生图/最新全能模型G-image2_4K放大版_极速生图_图像编辑_2046761253904846850.json, 图片生成/文生图/生图_洗图_Zimage双采样+Klein放大_2020509073417969666.json, 图片生成/文生图/高清洗图Zimage双采样放大Klein_2050607497655926786.json, 平台全量/Zimage-Klein高清洗图双采样放大_2058209852551421953.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Zimage-Klein高清洗图双采样放大_2058022601766821890.json、图片生成/图生图/高清洗图Zimage双采样Klein放大_2048324311714369537.json、图片生成/文生图/Zimage+生图+洗图+双采样+Klein放大_2070378304154193922.json、图片生成/文生图/最新全能模型G-image2_4K放大版_极速生图_图像编辑_2046761253904846850.json、图片生成/文生图/生图_洗图_Zimage双采样+Klein放大_2020509073417969666.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `Anything Everywhere` —— 6/7 个有
- `KSamplerAdvanced` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `easy clearCacheAll` —— 6/7 个有
- `workflow>LLama-ccp提示词反推` —— 6/7 个有
- `EmptyLatentImage` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `CR Image Input Switch` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `RH_RhartImageG2ImageToImage` —— 1/7 个有
- `RH_RhartImageG2TextToImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | res_multistep | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
