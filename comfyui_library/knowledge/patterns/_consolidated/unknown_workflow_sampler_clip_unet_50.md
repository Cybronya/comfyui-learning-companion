---
name: unknown_workflow_sampler_clip_unet_50
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.991067
common_nodes: [CLIPLoader, CLIPTextEncode, CM_IntToFloat, EmptyHunyuanLatentVideo, KSampler, Primitive integer [Crystools], UNETLoader, VAEDecodeTiled, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/反推提示词/64wsspwsb_2052437910317748225.json, 视频生成/图生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_1894981008754343938.json, 视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json, 视频生成/文生视频/Wan2.1(阿里万相)-文生视频_Comfyui工作流_1904365052583907330.json, 视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json, 视频生成/文生视频/Wan2.1文生视频_1985682376623828994.json, 视频生成/文生视频/Wan2.1文生视频_2008116883312087041.json, 视频生成/文生视频/文生视频 开源版_2046758506686058497.json, 视频生成/文生视频/文生视频+开源版 我的刀盾_2048961068537487362.json, 视频生成/文生视频/文生视频+开源版_2047284865078398977.json, 视频生成/文生视频/文生视频+开源版_2047564573158412289.json, 视频生成/文生视频/文生视频+开源版_2048571010336694273.json, 视频生成/文生视频/文生视频_1990234180640534529.json, 视频生成/文生视频/文生视频_2046503819072249858.json, 视频生成/文生视频/文生视频_Comfyui工作流_1958378106241368066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_50

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/64wsspwsb_2052437910317748225.json、视频生成/图生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_1894981008754343938.json、视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json、视频生成/文生视频/Wan2.1(阿里万相)-文生视频_Comfyui工作流_1904365052583907330.json、视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `Primitive integer [Crystools]`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 14/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `CreateVideo` —— 1/15 个有
- `Int` —— 1/15 个有
- `RTXVideoSuperResolution` —— 1/15 个有
- `SaveVideo` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 15 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 15 | 100% |
| 采样算法 | uni_pc | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 15/15 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：发现KSampler但没有VAEDecode
