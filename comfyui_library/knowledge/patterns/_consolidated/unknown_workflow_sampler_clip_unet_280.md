---
name: unknown_workflow_sampler_clip_unet_280
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.90175
common_nodes: [CLIPTextEncode, CreateVideo, DualCLIPLoader, ImageScale, KSampler, Kandinsky5ImageToVideo, LoadImage, ModelSamplingSD3, NormalizeVideoLatentStart, ReplaceVideoLatentFrames, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kandinsky 5.0 图生视频_1999008065406033921.json, 视频生成/图生视频/Kandinsky 5.0 +Qwen3 Vl自动图生视频_1999180009522819073.json, 视频生成/图生视频/Kandinsky 5.0 图生视频_1998819521249075201.json, 视频生成/图生视频/Kandinsky Qwen3高清图生视频_1999519750432714753.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_280

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kandinsky 5.0 图生视频_1999008065406033921.json、视频生成/图生视频/Kandinsky 5.0 +Qwen3 Vl自动图生视频_1999180009522819073.json、视频生成/图生视频/Kandinsky 5.0 图生视频_1998819521249075201.json、视频生成/图生视频/Kandinsky Qwen3高清图生视频_1999519750432714753.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `ImageScale`
- `KSampler`
- `Kandinsky5ImageToVideo`
- `LoadImage`
- `ModelSamplingSD3`
- `NormalizeVideoLatentStart`
- `ReplaceVideoLatentFrames`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
