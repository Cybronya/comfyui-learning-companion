---
name: unknown_workflow_video_sampler_clip_65
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.726444
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json, 视频生成/图生视频/Remix首尾帧生视频动态模型-官方工作流_2011093205202247682.json, 视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_1984504641570357250.json, 视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_2030191511907864578.json, 视频生成/图生视频/WAN2.2 RemixV2超高动态艺术激版首尾帧  可加速_1996163879166263297.json, 视频生成/图生视频/WAN2.2 RemixV2首尾帧动态_2017121557004423170.json, 视频生成/图生视频/Wan2.2_Remix（首尾帧)_2001276328982740993.json, 视频生成/图生视频/超高动态感增强  指定主题自动提示词图生视频  激版可加速_1998328006265438210.json, 视频生成/图生视频/超高动态感增强 艺术激版 图生视频 拒绝慢动作 可加速_1997659149460770818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json、视频生成/图生视频/Remix首尾帧生视频动态模型-官方工作流_2011093205202247682.json、视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_1984504641570357250.json、视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_2030191511907864578.json、视频生成/图生视频/WAN2.2 RemixV2超高动态艺术激版首尾帧  可加速_1996163879166263297.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 8/9 个有
- `CLIPVisionLoader` —— 8/9 个有
- `ModelPatchTorchSettings` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `WanFirstLastFrameToVideo` —— 7/9 个有
- `INTConstant` —— 6/9 个有
- `ImageResizeKJv2` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `RIFE VFI` —— 6/9 个有
- `easy clearCacheAll` —— 5/9 个有
- `wanBlockSwap` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `ImageConcatMulti` —— 3/9 个有
- `ImageResize+` —— 3/9 个有
- `Int` —— 3/9 个有
- `Qwen3_VQA` —— 3/9 个有
- `Text Multiline` —— 3/9 个有
- `MultiplePathsInput` —— 2/9 个有
- `PainterI2V` —— 2/9 个有
- `MultiTextConcatenate` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有
- `TextInput_` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 56% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 9 | 51% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler_ancestral | - | 9 | 78% |
| 重绘幅度 | simple | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，9 个样本
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，9 个样本，一致性 78%
- 重绘幅度 最常用 simple，9 个样本，一致性 89%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
