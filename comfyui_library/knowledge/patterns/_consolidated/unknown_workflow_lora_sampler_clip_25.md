---
name: unknown_workflow_lora_sampler_clip_25
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.985
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json, 视频生成/文生视频/1973317342270722050.json, 视频生成/文生视频/1973643031427551234.json, 视频生成/文生视频/1973778662703108098.json, 视频生成/文生视频/1978258359084310529.json, 视频生成/文生视频/1978705872639692801.json, 视频生成/文生视频/小工具 wan-alpha透明图层_2066720353575251968.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json、视频生成/文生视频/1973317342270722050.json、视频生成/文生视频/1973643031427551234.json、视频生成/文生视频/1973778662703108098.json、视频生成/文生视频/1978258359084310529.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageToMask` —— 6/7 个有
- `InvertMask` —— 5/7 个有
- `JoinImageWithAlpha` —— 5/7 个有
- `SaveVideoRGBA` —— 4/7 个有
- `SaveImage` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `SavePNGZIP_and_Preview_RGBA_AnimatedWEBP` —— 2/7 个有
- `INTConstant` —— 1/7 个有
- `ImageCompositeMasked` —— 1/7 个有
- `SaveAnimatedWEBP` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 7 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 7 | 0% |
| 采样算法 | uni_pc | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，7 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 uni_pc，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
