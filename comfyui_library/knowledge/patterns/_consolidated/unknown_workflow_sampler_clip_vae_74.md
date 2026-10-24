---
name: unknown_workflow_sampler_clip_vae_74
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.902
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DeepTranslatorTextNode, EmptyLatentImage, KSamplerSelect, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, VAEDecode, VAELoader, easy promptConcat, easy stylesSelector, workflow>模型加载区]
problems: []
missing: []
members: [图片生成/文生图/flux1双节棍文生图-带270风格和自动翻译节点_1976120206277914626.json, 图片生成/文生图/flux1文生图-带270多种风格 （输入中文即可）_1992207757744951297.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_74

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/flux1双节棍文生图-带270风格和自动翻译节点_1976120206277914626.json、图片生成/文生图/flux1文生图-带270多种风格 （输入中文即可）_1992207757744951297.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`
- `easy stylesSelector`
- `workflow>模型加载区`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | - | 2 | 97% |
| 高度 | 1472 | - | 2 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
