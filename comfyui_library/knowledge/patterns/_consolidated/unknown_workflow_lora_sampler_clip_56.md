---
name: unknown_workflow_lora_sampler_clip_56
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.702
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSampler, LoraLoader, ModelSamplingSD3, SaveVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan_vace_14B_ref2v.json, comfyui-workflow-templates-json/video_wan_vace_14B_t2v.json, comfyui-workflow-templates-json/video_wan_vace_outpainting.json, 视频生成/图生视频/video_wan_vace_flf2v_1954529424794370049.json, 视频生成/图生视频/wan_vace首尾帧生视频_1959350943030652929.json, 视频生成/图生视频/【老金驿站】满血阿里VACE4步极速图生视频_1926991420400500737.json, 视频生成/文生视频/wan_vace_14B图生视频_1959310423428378626.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan_vace_14B_ref2v.json、comfyui-workflow-templates-json/video_wan_vace_14B_t2v.json、comfyui-workflow-templates-json/video_wan_vace_outpainting.json、视频生成/图生视频/video_wan_vace_flf2v_1954529424794370049.json、视频生成/图生视频/wan_vace首尾帧生视频_1959350943030652929.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSampler`
- `LoraLoader`
- `ModelSamplingSD3`
- `SaveVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageToMask` —— 6/7 个有
- `MaskToImage` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `RepeatImageBatch` —— 6/7 个有
- `SaveAnimatedWEBP` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `SolidMask` —— 5/7 个有
- `ImageBatch` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `BatchImagesNode` —— 1/7 个有
- `GetVideoComponents` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `LoadVideo` —— 1/7 个有
- `RMBG` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.3 - 0.7 | 7 | 61% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |
| 采样步数 | 4 | 3 - 4 | 7 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | uni_pc | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.3 - 0.7，7 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 3 - 4，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
