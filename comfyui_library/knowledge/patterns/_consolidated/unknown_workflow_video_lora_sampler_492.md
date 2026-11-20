---
name: unknown_workflow_video_lora_sampler_492
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.475
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, INTConstant, ImageFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), SamplerCustom, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/WanAnimate2-动作迁移-角色替换_2096421447441932289.json, 平台全量/WanAnimate2最强动作迁移，无限循环长视频，丝滑完美_2096251526539993090.json, 视频生成/图生视频/WanAnimate2 动作迁移（效果最好的动作迁移）_2100492099857768449.json, 视频生成/图生视频/WanAnimate2-动作迁移双模式无限长视频【多人】_2098646467857698818.json, 视频生成/图生视频/WanAnimate2动作迁移_2096817694862565378.json, 视频生成/图生视频/王者归来！【WanAnimate2】最强动作迁移模型 丝滑长视频工作流_2095800669994311682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_492

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/WanAnimate2-动作迁移-角色替换_2096421447441932289.json、平台全量/WanAnimate2最强动作迁移，无限循环长视频，丝滑完美_2096251526539993090.json、视频生成/图生视频/WanAnimate2 动作迁移（效果最好的动作迁移）_2100492099857768449.json、视频生成/图生视频/WanAnimate2-动作迁移双模式无限长视频【多人】_2098646467857698818.json、视频生成/图生视频/WanAnimate2动作迁移_2096817694862565378.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `FeiHouWanAnimate2ToVideo` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `TrimVideoLatent` —— 5/6 个有
- `WanAnimate2ContextOptions` —— 5/6 个有
- `WanAnimate2ToVideo` —— 5/6 个有
- `FastGroupsBypassSwitch` —— 4/6 个有
- `FeiHouWanAnimate2SeamColorMatch` —— 4/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `WanAnimate2Cache` —— 3/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
