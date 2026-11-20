---
name: unknown_workflow_sampler_clip_unet_87
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.975385
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1956141417343143938.json, 图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1957735710319112194.json, 图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1958426008351358977.json, 图片生成/文生图/Wan2.2文生图片 真实摄影  细腻皮肤质感_1960618336759480321.json, 图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json, 视频生成/文生视频/Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json, 视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json, 视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json, 视频生成/文生视频/Wan2.2文生视频_2007645581098881026.json, 视频生成/文生视频/Wan2.2文生视频工作流_1963477743868547073.json, 视频生成/文生视频/Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1956141417343143938.json、图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1957735710319112194.json、图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1958426008351358977.json、图片生成/文生图/Wan2.2文生图片 真实摄影  细腻皮肤质感_1960618336759480321.json、图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 10/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `VHS_VideoCombine` —— 8/13 个有
- `Text` —— 6/13 个有
- `easy int` —— 6/13 个有
- `GetImageRangeFromBatch` —— 5/13 个有
- `SaveImage` —— 5/13 个有
- `Wan_video_prompt_generator` —— 5/13 个有
- `CFGZeroStar` —— 1/13 个有
- `WanVideoNAG` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 69% |
| Prompt 约束强度(CFG) | 14 | 6 - 20 | 13 | 61% |
| 采样算法 | 3.5 | 1 - 3.5 | 13 | 58% |
| 调度器 | euler | - | 13 | 92% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 69%
- Prompt 约束强度(CFG) 中位数 14，观测区间 6 - 20，13 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，13 个样本
- 调度器 最常用 euler，13 个样本，一致性 92%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
