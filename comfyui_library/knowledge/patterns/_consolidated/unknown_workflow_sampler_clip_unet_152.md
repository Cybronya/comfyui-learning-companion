---
name: unknown_workflow_sampler_clip_unet_152
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.927375
common_nodes: [CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2 JSON Multi-Panel Storyboard_2073788024386838530.json, 图片生成/图生图/Krea2 JSON多宫格分镜_2073304573829275649.json, 图片生成/文生图/Anima Preview3文生图_2042205608601985025.json, 图片生成/文生图/Anima Preview3文生图_2042597269245009921.json, 图片生成/文生图/Anima生图_2084612056606666754.json, 图片生成/文生图/Krea2 Clownshark × WanVAE Cinematic Engine_2072998793915965440.json, 图片生成/文生图/Krea2新采样成片引擎｜Clownshark×WanVAE质感版_2072703853161705474.json, 视频生成/文生视频/Krea2 随机提示词创作_2074464834908942338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_152

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2 JSON Multi-Panel Storyboard_2073788024386838530.json、图片生成/图生图/Krea2 JSON多宫格分镜_2073304573829275649.json、图片生成/文生图/Anima Preview3文生图_2042205608601985025.json、图片生成/文生图/Anima Preview3文生图_2042597269245009921.json、图片生成/文生图/Anima生图_2084612056606666754.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `FluxResolutionNode` —— 5/8 个有
- `ComfyUI-Krea2T-Enhancer` —— 3/8 个有
- `SDXLEmptyLatentSizePicker+` —— 2/8 个有
- `CreaPrompt` —— 1/8 个有
- `CreaPrompt_1` —— 1/8 个有
- `CreaPrompt_2` —— 1/8 个有
- `CreaPrompt_3` —— 1/8 个有
- `LatentUpscaleBy` —— 1/8 个有
- `LoraLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 832 | 6 | 94% |
| 高度 | 1280 | 1 - 1280 | 8 | 42% |
| 采样步数 | beta57 | - | 8 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 30 | 8 | 33% |
| 采样算法 | -1 | -1 - -1 | 8 | 100% |
| 调度器 | 1 | 0.45 - 1 | 8 | 80% |
| 重绘幅度 | 1 | 1 - 3 | 8 | 45% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 832，6 个样本，取值集中（一致性 94%）
- 高度 中位数 1280，观测区间 1 - 1280，8 个样本，取值分散，一致性仅 42%
- 采样步数 最常用 beta57，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 30，8 个样本，取值分散，一致性仅 33%
- 采样算法 中位数 -1，观测区间 -1 - -1，8 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 0.45 - 1，8 个样本，取值集中（一致性 80%）
- 重绘幅度 中位数 1，观测区间 1 - 3，8 个样本，取值分散，一致性仅 45%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
