---
name: unknown_workflow_video_sampler_clip_94
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.977429
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/通义万相Wan2.1图生视频GGUF量化16g显存可用_1895423724621529089.json, 视频生成/图生视频/通义万相Wan2.1图生视频_1895391021444497410.json, 视频生成/图生视频/（完成一半）怪兽抱抱WAN及PhotoDoodle视频工作流_1895732639271878658.json, 视频生成/文生视频/WAN2.1 万相图生视频，效果丝滑 拉布布360°旋转动画_1938037576559431682.json, 视频生成/文生视频/wan图片生成视频  视频动画_1922130213654708226.json, 视频生成/文生视频/熊猫快跑-视频动画_1933374904114786306.json, 视频生成/文生视频/通义万相ComfyuI原生图文转视频工作流-StarAI_1897394732773888001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/通义万相Wan2.1图生视频GGUF量化16g显存可用_1895423724621529089.json、视频生成/图生视频/通义万相Wan2.1图生视频_1895391021444497410.json、视频生成/图生视频/（完成一半）怪兽抱抱WAN及PhotoDoodle视频工作流_1895732639271878658.json、视频生成/文生视频/WAN2.1 万相图生视频，效果丝滑 拉布布360°旋转动画_1938037576559431682.json、视频生成/文生视频/wan图片生成视频  视频动画_1922130213654708226.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 5/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `UnetLoaderGGUF` —— 2/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `Note _O` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `SaveWEBM` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 7 | 81% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | uni_pc | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
