---
name: unknown_workflow_lora_sampler_unet_388
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.873
common_nodes: [CLIPLoader, CreateVideo, ImageCrop, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3ReferenceToVideo, PreviewImage, SaveVideo, UNETLoader_Any, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/MiniMax-H3_ORB360_漫画分格环绕_通用版_2117539686469160962.json, 视频生成/图生视频/MiniMax-H3_ORB360_漫画分格环绕_通用版_2109926051978760193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_388

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/MiniMax-H3_ORB360_漫画分格环绕_通用版_2117539686469160962.json、视频生成/图生视频/MiniMax-H3_ORB360_漫画分格环绕_通用版_2109926051978760193.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `ImageCrop`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3ReferenceToVideo`
- `PreviewImage`
- `SaveVideo`
- `UNETLoader_Any`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
