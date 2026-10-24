---
name: unknown_workflow_face_detailer_sampler_clip
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.780762
common_nodes: [AIO_Preprocessor, AnimaLLLiteApply, CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, FaceDetailer, ImageScale, LoadImage, NAGuidance, PreviewImage, RH_LLMAPI_Pro_Node, SAMLoader, SaveImage, Seed (rgthree), UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2056337290414346241.json, 图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2067974124164702209.json, 图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2067975826989207554.json, 图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2068919869478883330.json, 图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2074127159198834689.json, 图片生成/图生图/文生图+CN+修脸+修手_2069227698517528578.json, 图片生成/文生图/Anima-Base 文生图：CN 修脸与手部优化指南_2089715950257004545.json, 图片生成/文生图/Anima-Base 文生图：CN 修脸与手部优化指南_2089716086181814273.json, 图片生成/文生图/Anima-Base图生图+CN+修脸+修手_2055116648939565057.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2055109924421685249.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2061449188268920833.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2062559130791006210.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2065644656729350145.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2069748488539299841.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2070157364141060098.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2071584872338124801.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2078845019427008514.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2078859687012954113.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2079215800111681538.json, 图片生成/文生图/Anima-Base文生图+CN+修脸+修手_2080615905649848322.json, 图片生成/文生图/文生图+CN+修脸+修手_2069420520243810306.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_sampler_clip

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2056337290414346241.json、图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2067974124164702209.json、图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2067975826989207554.json、图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2068919869478883330.json、图片生成/图生图/Anima-Base文生图+CN+修脸+修手_2074127159198834689.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 21 个 workflow 都包含：
- `AIO_Preprocessor`
- `AnimaLLLiteApply`
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `FaceDetailer`
- `ImageScale`
- `LoadImage`
- `NAGuidance`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SAMLoader`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPSetLastLayer` —— 20/21 个有
- `EmptyLatentImage` —— 20/21 个有
- `FluxResolutionNode` —— 20/21 个有
- `LatentUpscaleBy` —— 20/21 个有
- `LoraLoaderModelOnly` —— 20/21 个有
- `Text` —— 20/21 个有
- `easy showAnything` —— 20/21 个有
- `Float` —— 1/21 个有
- `VAEEncode` —— 1/21 个有
- `image_scale_pixel_v2` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 20 | 100% |
| 高度 | 512 | 512 - 512 | 20 | 100% |
| 采样步数 | beta57 | - | 21 | 100% |
| Prompt 约束强度(CFG) | 30 | 30 - 30 | 21 | 100% |
| 采样算法 | -1 | -1 - -1 | 21 | 100% |
| 调度器 | 1 | 0.85 - 1 | 21 | 97% |
| 重绘幅度 | 3.01 | 3 - 3.01 | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，20 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，20 个样本，取值集中（一致性 100%）
- 采样步数 最常用 beta57，21 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 30，观测区间 30 - 30，21 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，21 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 0.85 - 1，21 个样本，取值集中（一致性 97%）
- 重绘幅度 中位数 3.01，观测区间 3 - 3.01，21 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3.01，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
