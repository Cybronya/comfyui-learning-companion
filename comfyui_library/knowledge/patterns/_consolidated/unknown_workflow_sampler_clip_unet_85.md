---
name: unknown_workflow_sampler_clip_unet_85
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.942
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1950503480169517058.json, 视频生成/文生视频/wan2.2工作流_2034980882162917377.json, 视频生成/文生视频/1950456441427693570.json, 视频生成/文生视频/wan2.2文生视频_2087718119883235330.json, 视频生成/文生视频/wan文生视频_2009970396799442946.json, 视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json, 视频生成/文生视频/文生视频工作流_2066457517043044354.json, 视频生成/文生视频/新版 Wan2.2_Lightning_Palingenesis 精品免费课程对应工作流 ____1974007898521120769.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_85

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/1950503480169517058.json、视频生成/文生视频/wan2.2工作流_2034980882162917377.json、视频生成/文生视频/1950456441427693570.json、视频生成/文生视频/wan2.2文生视频_2087718119883235330.json、视频生成/文生视频/wan文生视频_2009970396799442946.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `RIFE VFI` —— 2/8 个有
- `SaveAnimatedWEBP` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `SaveWEBM` —— 1/8 个有
- `TorchCompileModel` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 50% |
| Prompt 约束强度(CFG) | 9 | 4 - 20 | 8 | 39% |
| 采样算法 | 1.75 | 1 - 3.5 | 8 | 45% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 9，观测区间 4 - 20，8 个样本，取值分散，一致性仅 39%
- 采样算法 中位数 1.75，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 45%
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
