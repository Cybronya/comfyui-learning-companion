---
name: unknown_workflow_sampler_clip_unet_74
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.986875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json, 视频生成/文生视频/1930295791557185537.json, 视频生成/文生视频/1973317342270722050.json, 视频生成/文生视频/1973643031427551234.json, 视频生成/文生视频/1973778662703108098.json, 视频生成/文生视频/1978258359084310529.json, 视频生成/文生视频/1978705872639692801.json, 视频生成/文生视频/小工具 wan-alpha透明图层_2066720353575251968.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json、视频生成/文生视频/1930295791557185537.json、视频生成/文生视频/1973317342270722050.json、视频生成/文生视频/1973643031427551234.json、视频生成/文生视频/1973778662703108098.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `ImageToMask` —— 6/8 个有
- `InvertMask` —— 5/8 个有
- `JoinImageWithAlpha` —— 5/8 个有
- `SaveVideoRGBA` —— 4/8 个有
- `VHS_VideoCombine` —— 4/8 个有
- `SaveImage` —— 3/8 个有
- `SaveAnimatedWEBP` —— 2/8 个有
- `SavePNGZIP_and_Preview_RGBA_AnimatedWEBP` —— 2/8 个有
- `INTConstant` —— 1/8 个有
- `ImageCompositeMasked` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 8 | 5% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 8 | 4% |
| 采样算法 | uni_pc | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，8 个样本，取值分散，一致性仅 5%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，8 个样本，取值分散，一致性仅 4%
- 采样算法 最常用 uni_pc，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
