---
name: image_to_image_face_detailer_lora_sampler
type: Image To Image
frequency: 2
level: weak
coverage: 0.6075
common_nodes: [CFGZeroStarAndInit, CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner, CheckpointLoaderSimple, CheckpointLoader|pysssss, EmptyLatentImage, FaceDetailerPipe, Fast Bypasser (rgthree), GetNode, ImageScaleBy, KSampler, LoadImage, Lora Loader Stack (rgthree), Pack SDXL Tuple, PrimitiveString, RH_LLMAPI_NODE, SAMLoader, SaveImage, Seed (rgthree), SetNode, ShowText|pysssss, SiliconflowLLM, Text Multiline, TextInput_, ToDetailerPipe, UltralyticsDetectorProvider, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: []
missing: []
members: [图片生成/文生图/SDXL 基础文生图-API_1934792295801626625.json, 图片生成/文生图/SDXL 基础文生图_1908008346551463937.json]
source: knowledge_consolidation
---

# image_to_image_face_detailer_lora_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/SDXL 基础文生图-API_1934792295801626625.json、图片生成/文生图/SDXL 基础文生图_1908008346551463937.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPTextEncodeSDXL`
- `CLIPTextEncodeSDXLRefiner`
- `CheckpointLoaderSimple`
- `CheckpointLoader|pysssss`
- `EmptyLatentImage`
- `FaceDetailerPipe`
- `Fast Bypasser (rgthree)`
- `GetNode`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `Pack SDXL Tuple`
- `PrimitiveString`
- `RH_LLMAPI_NODE`
- `SAMLoader`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `SiliconflowLLM`
- `Text Multiline`
- `TextInput_`
- `ToDetailerPipe`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `KSampler SDXL (Eff.)` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `SaveLatent` —— 1/2 个有
- `Unpack SDXL Tuple` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 12.75 | - | 2 | 43% |
| 采样算法 | 5.5 | - | 1 | 100% |
| 调度器 | heun | - | 2 | 50% |
| 重绘幅度 | 18 | - | 1 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 12.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 43%
- 调度器 最常用 heun，2 个样本，一致性 50%
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 18，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
