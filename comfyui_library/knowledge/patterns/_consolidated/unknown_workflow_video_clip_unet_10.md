---
name: unknown_workflow_video_clip_unet_10
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, ModelSamplingSD3, TrimVideoLatent, UNETLoader, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/1967578038525390850.json, 视频生成/文生视频/1967620116848545793.json, 视频生成/文生视频/1967630045374287873.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-图生视频_1982048372632764418.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-姿态视频引导加参考_1982051642445045761.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-首尾帧_1982051197618135041.json, 视频生成/文生视频/Wan 2.2-Fun-VACE-图生视频_2072999574413025280.json, 视频生成/文生视频/Wan 2.2-Fun-VACE-姿态视频引导加参考无敌控_2072999574836649984.json, 视频生成/文生视频/Wan 2.2-Fun-VACE-首尾帧_2072999573054070784.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/1967578038525390850.json、视频生成/文生视频/1967620116848545793.json、视频生成/文生视频/1967630045374287873.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-图生视频_1982048372632764418.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-姿态视频引导加参考_1982051642445045761.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `VAELoader` —— 6/9 个有
- `WanVideoVACEStartToEndFrame` —— 6/9 个有
- `AIO_Preprocessor` —— 3/9 个有
- `AV_VAELoader` —— 3/9 个有
- `ImageRepeat` —— 3/9 个有
- `KSampler` —— 3/9 个有
- `Miaoshouai_Tagger` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 44% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 9 | 46% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 9 | 44% |
| 重绘幅度 | simple | - | 9 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 44%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，9 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 44%
- 重绘幅度 最常用 simple，9 个样本，一致性 67%
