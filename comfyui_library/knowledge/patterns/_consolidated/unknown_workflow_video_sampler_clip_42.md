---
name: unknown_workflow_video_sampler_clip_42
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.970667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1950503507558387713.json, 视频生成/文生视频/wan2.2工作流_2034980882162917377.json, 视频生成/文生视频/1950456441427693570.json, 视频生成/文生视频/wan2.2文生视频_2087718119883235330.json, 视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json, 视频生成/文生视频/wan文生视频_2009970396799442946.json, 视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json, 视频生成/文生视频/工作流视频篇1-阿里万相Wan2.2Al视频创作实战_2016870256769245185.json, 视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json, 视频生成/文生视频/文生视频Holocine电影分镜工作流（自己测试吧）_1985283263507873793.json, 视频生成/文生视频/电影分镜创作test_1982334497687519233.json, "视频生成/文生视频/纯净万相 Wan2.2-Remix-Comfy-T2V-文生视频 不带lora,带插帧丝滑_2042646743598243841.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/1950503507558387713.json、视频生成/文生视频/wan2.2工作流_2034980882162917377.json、视频生成/文生视频/1950456441427693570.json、视频生成/文生视频/wan2.2文生视频_2087718119883235330.json、视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 10/12 个有
- `PathchSageAttentionKJ` —— 9/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `INTConstant` —— 4/12 个有
- `RIFE VFI` —— 2/12 个有
- `UnetLoaderGGUF` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `Int` —— 1/12 个有
- `MuyeMathCalculator` —— 1/12 个有
- `WanVideoNAG` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 58% |
| Prompt 约束强度(CFG) | 12 | 4 - 20 | 12 | 50% |
| 采样算法 | 1.75 | 1 - 3.5 | 12 | 45% |
| 调度器 | euler | - | 12 | 92% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 58%
- Prompt 约束强度(CFG) 中位数 12，观测区间 4 - 20，12 个样本，取值分散，一致性仅 50%
- 采样算法 中位数 1.75，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 45%
- 调度器 最常用 euler，12 个样本，一致性 92%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
