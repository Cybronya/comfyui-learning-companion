---
name: unknown_workflow_video_sampler_clip_73
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.58975
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/NBA探班一镜到底_2016088168881201153.json, 图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json, 图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json, 图片生成/图生图/WAN2.2-RemixV2-I2V首尾帧_2002505189661786113.json, 图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json, 视频生成/图生视频/Wan2.2+Qwen3VL+Foley多模态全自动图生视频_2076490092809637889.json, 视频生成/图生视频/演唱会 + 名人探班视频一镜到底工作流_2009656283015684097.json, 视频生成/图生视频/（再来王炸）片场探班一镜到底_2003358593732771842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/NBA探班一镜到底_2016088168881201153.json、图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json、图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json、图片生成/图生图/WAN2.2-RemixV2-I2V首尾帧_2002505189661786113.json、图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `MultiplePathsInput` —— 7/8 个有
- `Qwen3_VQA` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `ImageLoader` —— 6/8 个有
- `ImageResizeKJv2` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `ModelPatchTorchSettings` —— 5/8 个有
- `RIFE VFI` —— 5/8 个有
- `WanFirstLastFrameToVideo` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `Any To Any` —— 3/8 个有
- `CR Text Replace` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `Pick From Batch (mtb)` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `VHS_SelectFilename` —— 3/8 个有
- `WanImageToVideo` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `HunyuanVideoFoley` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `RH_Nano_Banana2_Image2Image` —— 2/8 个有
- `easy float` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoadVideo` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | normal | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 normal，8 个样本，一致性 100%
