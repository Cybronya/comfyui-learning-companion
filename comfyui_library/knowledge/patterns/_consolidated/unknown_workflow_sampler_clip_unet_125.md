---
name: unknown_workflow_sampler_clip_unet_125
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.803333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImageScaleBy, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PrimitiveStringMultiline, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/SMOOTH 图生视频 1.5_1985245906587033602.json, 视频生成/图生视频/Smooth图生视频-梵高走出星空_1984048201416245250.json, 视频生成/图生视频/WAN 2.2 Smooth Mix图生视频_1981294869803073538.json, 视频生成/图生视频/WAN 2.2 Smooth Workflow v2.0 (img2vid)_2021178894228918274.json, 视频生成/图生视频/WAN22 SmoothMix首尾帧_1986011600907841537.json, 视频生成/图生视频/wan2.2-GGUF+SmoothMix图生视频工作流_2006660938727952385.json, 视频生成/图生视频/wan2.2官方图生视频+Smooth 2.2动态优化+自动提示词_1983333336628273153.json, 视频生成/图生视频/（自用）Wan2.2 Smooth Mix高低噪模型高动态图生视频V1（KJ版）_1979918269014511617.json, 视频生成/图生视频/🦖WAN 2.2 Smooth高质量图生视频_1980114227547508737.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/SMOOTH 图生视频 1.5_1985245906587033602.json、视频生成/图生视频/Smooth图生视频-梵高走出星空_1984048201416245250.json、视频生成/图生视频/WAN 2.2 Smooth Mix图生视频_1981294869803073538.json、视频生成/图生视频/WAN 2.2 Smooth Workflow v2.0 (img2vid)_2021178894228918274.json、视频生成/图生视频/WAN22 SmoothMix首尾帧_1986011600907841537.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Pick From Batch (mtb)` —— 8/9 个有
- `RIFE VFI` —— 8/9 个有
- `SaveImage` —— 8/9 个有
- `Seed (rgthree)` —— 8/9 个有
- `StringConcatenate` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `WanImageToVideo` —— 8/9 个有
- `easy showAnything` —— 8/9 个有
- `ColorMatch` —— 7/9 个有
- `JWInteger` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `UnetLoaderGGUF` —— 3/9 个有
- `Qwen3_VQA` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `mxSlider2D` —— 2/9 个有
- `Bjornulf_ShowInt` —— 1/9 个有
- `CR Text List To String` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `Power Lora Loader (rgthree)` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有
- `TT_img_enc_v2` —— 1/9 个有
- `WanFirstLastFrameToVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 56% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 9 | 87% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler_ancestral | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，9 个样本，取值集中（一致性 87%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
