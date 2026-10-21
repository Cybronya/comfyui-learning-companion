---
name: unknown_workflow_upscale_latent_upscale_lora_10
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.788333
common_nodes: [AIO_Preprocessor, AnimaLLLiteApply, CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, EmptyLatentImage, FluxResolutionNode, ImageScale, LatentUpscaleBy, LoadImage, LoraLoaderModelOnly, NAGuidance, PreviewImage, SaveImage, Text, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima-Base 文生图：CN 修脸与手部优化指南_2089715950257004545.json, 图片生成/文生图/Anima-Base 文生图：CN 修脸与手部优化指南_2089716086181814273.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2055109924421685249.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2061449188268920833.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2062559130791006210.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2065644656729350145.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2069748488539299841.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2070157364141060098.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2071584872338124801.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2078845019427008514.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2078859687012954113.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2079215800111681538.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2080615905649848322.json, 图片生成/文生图/anima&CN_2057391382855241730.json, 图片生成/文生图/文生图+CN+修脸+修手_2069420520243810306.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Anima-Base 文生图：CN 修脸与手部优化指南_2089715950257004545.json、图片生成/文生图/Anima-Base 文生图：CN 修脸与手部优化指南_2089716086181814273.json、图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2055109924421685249.json、图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2061449188268920833.json、图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2062559130791006210.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 15 个 workflow 都包含：
- `AIO_Preprocessor`
- `AnimaLLLiteApply`
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `ImageScale`
- `LatentUpscaleBy`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NAGuidance`
- `PreviewImage`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPSetLastLayer` —— 14/15 个有
- `FaceDetailer` —— 14/15 个有
- `RH_LLMAPI_Pro_Node` —— 14/15 个有
- `SAMLoader` —— 14/15 个有
- `Seed (rgthree)` —— 14/15 个有
- `UltralyticsDetectorProvider` —— 14/15 个有
- `easy showAnything` —— 14/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 15 | 100% |
| 高度 | 512 | 512 - 512 | 15 | 100% |
| 采样步数 | beta57 | - | 15 | 100% |
| Prompt 约束强度(CFG) | 30 | 30 - 30 | 15 | 100% |
| 采样算法 | -1 | -1 - -1 | 15 | 100% |
| 调度器 | 1 | 0.55 - 1 | 15 | 88% |
| 重绘幅度 | 3.01 | 2.88 - 3.01 | 15 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，15 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，15 个样本，取值集中（一致性 100%）
- 采样步数 最常用 beta57，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 30，观测区间 30 - 30，15 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，15 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 0.55 - 1，15 个样本，取值集中（一致性 88%）
- 重绘幅度 中位数 3.01，观测区间 2.88 - 3.01，15 个样本，取值集中（一致性 99%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3.01，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
