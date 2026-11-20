---
name: unknown_workflow_lora_sampler_clip_100
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.9505
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageToMask, InvertMask, JoinImageWithAlpha, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json, 平台全量/123123123_1977905569497579521.json, 平台全量/AI视频抠图大师：Wan-Alpha，生成没有背景图的宠物狗展示视频_1975387186184982530.json, 平台全量/透明视频生成_1990675594662862850.json, 视频生成/文生视频/wan-alpha透明视频素材制作_1978258359084310529.json, 视频生成/文生视频/小工具 wan-alpha透明图层_1973643031427551234.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_100

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json、平台全量/123123123_1977905569497579521.json、平台全量/AI视频抠图大师：Wan-Alpha，生成没有背景图的宠物狗展示视频_1975387186184982530.json、平台全量/透明视频生成_1990675594662862850.json、视频生成/文生视频/wan-alpha透明视频素材制作_1978258359084310529.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImageToMask`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 4/6 个有
- `SaveVideoRGBA` —— 4/6 个有
- `SaveAnimatedWEBP` —— 2/6 个有
- `CR SDXL Aspect Ratio` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 6 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 6 | 12% |
| 采样算法 | uni_pc | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，6 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，6 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 uni_pc，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
