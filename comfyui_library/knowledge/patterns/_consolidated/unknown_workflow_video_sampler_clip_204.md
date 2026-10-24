---
name: unknown_workflow_video_sampler_clip_204
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.625
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/超高动态感增强  指定主题自动提示词图生视频  激版可加速_1998328006265438210.json, 视频生成/图生视频/超高动态感增强 艺术激版 图生视频 拒绝慢动作 可加速_1997659149460770818.json, 视频生成/文生视频/Remix V2自动提示词 指定主题文生视频 激版可加速_1996172042313646082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_204

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/超高动态感增强  指定主题自动提示词图生视频  激版可加速_1998328006265438210.json、视频生成/图生视频/超高动态感增强 艺术激版 图生视频 拒绝慢动作 可加速_1997659149460770818.json、视频生成/文生视频/Remix V2自动提示词 指定主题文生视频 激版可加速_1996172042313646082.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RIFE VFI`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MultiTextConcatenate` —— 2/3 个有
- `MuyeTextEditOutput` —— 2/3 个有
- `PainterI2V` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
