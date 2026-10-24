---
name: unknown_workflow_video_clip_vae_3
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.968333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/3分钟完成_文生视频6s(97帧)——wan2.2  GGUF_1958137179354574850.json, 视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json, 视频生成/文生视频/【最接近官方】Lightx2v-T2V-4步快速文生视频_1972827331947614209.json, 视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json, 视频生成/文生视频/工作流视频篇1-阿里万相Wan2.2Al视频创作实战_2016870256769245185.json, 视频生成/文生视频/文生视频工作流_2066457517043044354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/3分钟完成_文生视频6s(97帧)——wan2.2  GGUF_1958137179354574850.json、视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json、视频生成/文生视频/【最接近官方】Lightx2v-T2V-4步快速文生视频_1972827331947614209.json、视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json、视频生成/文生视频/工作流视频篇1-阿里万相Wan2.2Al视频创作实战_2016870256769245185.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ModelSamplingSD3` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `UNETLoader` —— 4/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `CFGZeroStar` —— 1/6 个有
- `WanMoeKSampler` —— 1/6 个有
- `wanBlockSwap` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 6 | 16% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 34% |
| 调度器 | euler | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，6 个样本，取值分散，一致性仅 16%
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 调度器 最常用 euler，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 83%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
