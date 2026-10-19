---
name: unknown_workflow_video_sampler_clip_143
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6245
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2043951609989828610.json, 视频生成/图生视频/1986984550565916673.json, 视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json, 视频生成/文生视频/文生视频无限制自动扩写三解码_1988443693134823426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2043951609989828610.json、视频生成/图生视频/1986984550565916673.json、视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json、视频生成/文生视频/文生视频无限制自动扩写三解码_1988443693134823426.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `RIFE VFI` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `HunyuanVideoFoley` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `QZ_ResolutionPreset` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveLatent` —— 1/4 个有
- `TT_img_enc_v2` —— 1/4 个有
- `TextConcat` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 4 | 88% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，4 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，4 个样本，一致性 75%
