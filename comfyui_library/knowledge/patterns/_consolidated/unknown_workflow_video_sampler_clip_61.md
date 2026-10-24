---
name: unknown_workflow_video_sampler_clip_61
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.571444
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, MultiplePathsInput, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/NBA探班一镜到底_2016088168881201153.json, 图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json, 图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json, 图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json, 视频生成/图生视频/Wan2.2+Qwen3VL+Foley多模态全自动图生视频_2076490092809637889.json, 视频生成/图生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-视频-声音_1987069561856004097.json, 视频生成/图生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-首尾帧-声音_1987091319136956418.json, 视频生成/图生视频/演唱会 + 名人探班视频一镜到底工作流_2009656283015684097.json, 视频生成/图生视频/（再来王炸）片场探班一镜到底_2003358593732771842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/NBA探班一镜到底_2016088168881201153.json、图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json、图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json、图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json、视频生成/图生视频/Wan2.2+Qwen3VL+Foley多模态全自动图生视频_2076490092809637889.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `ImageLoader` —— 6/9 个有
- `ModelPatchTorchSettings` —— 6/9 个有
- `RIFE VFI` —— 6/9 个有
- `Any To Any` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `VHS_SelectFilename` —— 5/9 个有
- `WanFirstLastFrameToVideo` —— 5/9 个有
- `HunyuanVideoFoley` —— 4/9 个有
- `LayerUtility: PurgeVRAM V2` —— 4/9 个有
- `WanImageToVideo` —— 4/9 个有
- `easy float` —— 4/9 个有
- `CR Text Replace` —— 3/9 个有
- `LayerUtility: PurgeVRAM` —— 3/9 个有
- `Pick From Batch (mtb)` —— 3/9 个有
- `SaveImage` —— 3/9 个有
- `Text Multiline` —— 3/9 个有
- `RH_Nano_Banana2_Image2Image` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoadVideo` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | normal | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 normal，9 个样本，一致性 100%
