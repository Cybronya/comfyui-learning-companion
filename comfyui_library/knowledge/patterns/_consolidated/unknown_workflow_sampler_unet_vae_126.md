---
name: unknown_workflow_sampler_unet_vae_126
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.83125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2 多图参考图像编辑_2073314422151540738.json, 图片生成/图生图/Krea2-多图参考-多图融合-视觉设计-时尚摄影_2073903914298208257.json, 图片生成/图生图/Krea2-多图参考-多图融合-视觉设计-时尚摄影_2074305885173800961.json, 图片生成/图生图/Krea2-多图参考-多图融合-视觉设计-时尚摄影_2074417216031911938.json, 图片生成/图生图/krea2图像编辑_2072941442527490050.json, 图片生成/图生图/图像编辑- KREA V2_2073342522730041345.json, 图片生成/图生图/多图编辑- Krea2_2073339264804409345.json, 图片生成/文生图/Krea2 Multi-Image Reference Editing_2073788017583673345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_126

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2 多图参考图像编辑_2073314422151540738.json、图片生成/图生图/Krea2-多图参考-多图融合-视觉设计-时尚摄影_2073903914298208257.json、图片生成/图生图/Krea2-多图参考-多图融合-视觉设计-时尚摄影_2074305885173800961.json、图片生成/图生图/Krea2-多图参考-多图融合-视觉设计-时尚摄影_2074417216031911938.json、图片生成/图生图/krea2图像编辑_2072941442527490050.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Krea2EditRebalance` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `ComfyUI-Krea2T-Enhancer` —— 3/8 个有
- `ConditioningConcat` —— 3/8 个有
- `ConditioningKrea2Rebalance` —— 3/8 个有
- `Krea2EncodeRebalance` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `RMBG` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 8 | 100% |
| 高度 | 1024 | 1024 - 1024 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
