---
name: unknown_workflow_clip_unet_vae_13
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8266
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, CreateVideo, GetVideoComponents, LoadImage, LoadVideo, ModelSamplingSD3, PreviewImage, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json, comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json, comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json, 平台全量/WAN-线稿控制_1994225191316373505.json, 平台全量/wan2.2-动作迁移-加速lora-4步极速-14B_fun_control_1956361254153670657.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json、comfyui-workflow-templates-json/video_wan2_2_5B_fun_control.json、comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json、平台全量/WAN-线稿控制_1994225191316373505.json、平台全量/wan2.2-动作迁移-加速lora-4步极速-14B_fun_control_1956361254153670657.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `CreateVideo`
- `GetVideoComponents`
- `LoadImage`
- `LoadVideo`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 3/5 个有
- `Wan22FunControlToVideo` —— 3/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `SaveAnimatedWEBP` —— 2/5 个有
- `TrimVideoLatent` —— 2/5 个有
- `WanVaceToVideo` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `Int` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 3 | 19% |
| Prompt 约束强度(CFG) | 4 | 1 - 20 | 5 | 0% |
| 采样算法 | uni_pc | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.3 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，3 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 20，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 uni_pc，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
