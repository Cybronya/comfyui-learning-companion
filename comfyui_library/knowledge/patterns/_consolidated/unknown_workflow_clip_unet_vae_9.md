---
name: unknown_workflow_clip_unet_vae_9
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima生图_2084612056606666754.json, 图片生成/文生图/Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440.json, 图片生成/文生图/Krea2新采样成片引擎｜Clownshark×WanVAE质感版_2072703853161705474.json, 图片生成/文生图/文生图工作流_2087111210465579009.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Anima生图_2084612056606666754.json、图片生成/文生图/Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440.json、图片生成/文生图/Krea2新采样成片引擎｜Clownshark×WanVAE质感版_2072703853161705474.json、图片生成/文生图/文生图工作流_2087111210465579009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ClownsharKSampler_Beta` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `FluxResolutionNode` —— 2/4 个有
- `KRestartSamplerSimple` —— 1/4 个有
- `LoraLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 宽度 | 744 | 720 - 832 | 4 | 94% |
| 高度 | 1152 | 768 - 1280 | 4 | 80% |
| 采样步数 | beta57 | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 28 | 3 | 36% |
| 采样算法 | -1 | -1 - -1 | 3 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | 1 | 1 - 3 | 3 | 43% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 744，观测区间 720 - 832，4 个样本，取值集中（一致性 94%）
- 高度 中位数 1152，观测区间 768 - 1280，4 个样本，取值集中（一致性 80%）
- 采样步数 最常用 beta57，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 28，3 个样本，取值分散，一致性仅 36%
- 采样算法 中位数 -1，观测区间 -1 - -1，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
