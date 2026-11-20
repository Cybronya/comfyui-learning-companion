---
name: unknown_workflow_video_lora_clip_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8555
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetNode, ImageConcatMulti, ImageResizeKJv2, Int, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/wan_alpha_t2v_14B-透明视频_1977197934913703938.json, 视频生成/文生视频/Wan2.2-4steps-250928-dyno-high-lightx2v-文生视频_1976432692420059138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/wan_alpha_t2v_14B-透明视频_1977197934913703938.json、视频生成/文生视频/Wan2.2-4steps-250928-dyno-high-lightx2v-文生视频_1976432692420059138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageToMask` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `JoinImageWithAlpha` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `SaveVideoRGBA` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 29% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 29%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
