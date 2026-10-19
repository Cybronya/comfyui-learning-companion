---
name: text_to_image_video_upscale_lora
type: Text To Image
frequency: 15
level: strong
coverage: 0.887733
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3导演台ref2va，全能参考图生视频方案_2111237770525106178.json, 视频生成/图生视频/MiniMax H3导演台人物去油，图生视频全能方案_2111289077042601985.json, 视频生成/图生视频/MiniMax H3导演台全能fl2v流程，图生视频导演级运镜_2110444159667625985.json, 视频生成/图生视频/MiniMax H3导演台全能工作流｜无水印版视频生成_2095281363539808258.json, 视频生成/图生视频/导演台ref2va工作流｜MiniMax H3图生视频直出_2091667555638398977.json, 视频生成/图生视频/导演台全能工作流fl2v｜MiniMax H3图生视频直出_2091592035697516546.json, 视频生成/图生视频/导演台全能工作流｜MiniMax H3 ref2va全能参考_2090897981406015489.json, 视频生成/图生视频/无水印导演台全能流｜MiniMax H3开源角色设计图生视频_2092719967396524033.json, 视频生成/图生视频/无水印版开源导演台｜MiniMax H3场景特效图生视频_2092919674605498369.json, 视频生成/文生视频/H3图生视频高清版 无水印高清视频生成工具_2099215533198635010.json, 视频生成/文生视频/H3图生视频高清版 无水印高清视频生成工具_2099595930357035010.json, 视频生成/文生视频/MiniMax H3 Director全能参考视频导演台 无水印输出版_2098271585596694529.json, 视频生成/文生视频/MiniMax H3 Max转场导演台全能参考首尾帧视频处理工具_2102145394816933889.json, 视频生成/文生视频/fl2v导演台全能｜MiniMax H3文生视频生成_2092894391294849025.json, 视频生成/文生视频/导演台全能工作流fl2v版｜MiniMax H3文生视频_2090908366989250561.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3导演台ref2va，全能参考图生视频方案_2111237770525106178.json、视频生成/图生视频/MiniMax H3导演台人物去油，图生视频全能方案_2111289077042601985.json、视频生成/图生视频/MiniMax H3导演台全能fl2v流程，图生视频导演级运镜_2110444159667625985.json、视频生成/图生视频/MiniMax H3导演台全能工作流｜无水印版视频生成_2095281363539808258.json、视频生成/图生视频/导演台ref2va工作流｜MiniMax H3图生视频直出_2091667555638398977.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3Director` —— 13/15 个有
- `PreviewAny` —— 7/15 个有
- `SaveImage` —— 7/15 个有
- `CR Load LoRA` —— 2/15 个有
- `ComfyMiniMaxH3Director` —— 2/15 个有
- `CustomCombo` —— 2/15 个有
- `StringToNumber` —— 2/15 个有
- `TextSwitchCase` —— 2/15 个有
- `CR Text` —— 1/15 个有
- `DapaoImageSplitNode` —— 1/15 个有
- `LoadImage` —— 1/15 个有
- `Switch` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
