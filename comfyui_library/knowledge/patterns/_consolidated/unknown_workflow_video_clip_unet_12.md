---
name: unknown_workflow_video_clip_unet_12
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.96575
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1902680529605668865.json, 视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json, 视频生成/文生视频/Wan2.1-720P-SLG-文生视频_2072999848967970816.json, 视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json, 视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json, 视频生成/文生视频/Wan2.2Remix高质量文生视频_1988716572640423937.json, 视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json, 视频生成/文生视频/1937731773860352001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/1902680529605668865.json、视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json、视频生成/文生视频/Wan2.1-720P-SLG-文生视频_2072999848967970816.json、视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json、视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 7/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `KSampler` —— 4/8 个有
- `KSamplerAdvanced` —— 4/8 个有
- `WanVideoTeaCacheKJ` —— 4/8 个有
- `INTConstant` —— 3/8 个有
- `WanVideoEnhanceAVideoKJ` —— 3/8 个有
- `SkipLayerGuidanceWanVideo` —— 2/8 个有
- `TorchCompileModelWanVideo` —— 2/8 个有
- `Int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 9 | 6 - 30 | 8 | 32% |
| 采样算法 | 1 | 1 - 3.5 | 4 | 33% |
| 调度器 | euler | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 9，观测区间 6 - 30，8 个样本，取值分散，一致性仅 32%
- 采样算法 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
