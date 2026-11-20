---
name: unknown_workflow_generic_1302
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.799
common_nodes: [MultiplePathsInput, Qwen3_VQA, RH_Sora2_T2V, SaveVideo, VideoLoader, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3VL：全系反推提示词，解析图像 DNA，精准复刻！_1981862000647127042.json, 视频生成/文生视频/【阡陌】Qwen3-VL视频反推提示词全能视频S自动文生视频_1983422798716706818.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1302

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Qwen3VL：全系反推提示词，解析图像 DNA，精准复刻！_1981862000647127042.json、视频生成/文生视频/【阡陌】Qwen3-VL视频反推提示词全能视频S自动文生视频_1983422798716706818.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `MultiplePathsInput`
- `Qwen3_VQA`
- `RH_Sora2_T2V`
- `SaveVideo`
- `VideoLoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageLoader` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
