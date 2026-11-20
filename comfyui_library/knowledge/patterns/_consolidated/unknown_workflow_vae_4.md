---
name: unknown_workflow_vae_4
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.875429
common_nodes: [CreateVideo, LoadImage, PrimitiveStringMultiline, RHMiniMaxH3ModelLoader, RHMiniMaxH3RefGen, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/H3双采口播工作流｜照片+文案自动配音数字人_2095417328619057153.json, 视频生成/图生视频/H3音画同步-参考视频工作流_2094956326815358978.json, 视频生成/图生视频/MiniMax H3上下文参考视频+图生视频-融合运镜与角色工作流_2096427200533848066.json, 视频生成/图生视频/MiniMax H3上下文多参考生视频-多图融合工作流_2096426983138877441.json, 视频生成/图生视频/MiniMax H3全能参考-图音视频多素材再生工作流_2095040014278287362.json, 视频生成/图生视频/MiniMax H3全能参考30秒-图音视频多素材拼接工作流_2096903622029303810.json, 视频生成/图生视频/MiniMax H3全能参考60秒-图音视频多素材拼接工作流_2096903657953513473.json]
source: knowledge_consolidation
---

# unknown_workflow_vae_4

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3双采口播工作流｜照片+文案自动配音数字人_2095417328619057153.json、视频生成/图生视频/H3音画同步-参考视频工作流_2094956326815358978.json、视频生成/图生视频/MiniMax H3上下文参考视频+图生视频-融合运镜与角色工作流_2096427200533848066.json、视频生成/图生视频/MiniMax H3上下文多参考生视频-多图融合工作流_2096426983138877441.json、视频生成/图生视频/MiniMax H3全能参考-图音视频多素材再生工作流_2095040014278287362.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CreateVideo`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RHMiniMaxH3ModelLoader`
- `RHMiniMaxH3RefGen`
- `RHMiniMaxH3TextEncoderLoader`
- `RHMiniMaxH3VAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 4/7 个有
- `LoadVideo` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `Video Slice` —— 3/7 个有
- `VideoConcatenate` —— 2/7 个有
- `OmniVoiceVoiceDesignTTS` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
