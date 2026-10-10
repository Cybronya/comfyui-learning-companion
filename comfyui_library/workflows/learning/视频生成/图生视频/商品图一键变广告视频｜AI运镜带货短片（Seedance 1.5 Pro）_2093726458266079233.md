---
key: 视频生成/图生视频/商品图一键变广告视频｜AI运镜带货短片（Seedance 1.5 Pro）_2093726458266079233.json
name: 商品图一键变广告视频｜AI运镜带货短片（Seedance 1.5 Pro）_2093726458266079233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/商品图一键变广告视频｜AI运镜带货短片（Seedance 1.5 Pro）_2093726458266079233.json
hash: f1c06feccb3cc2e9
coverage: 0.875
learned_at: 2026-10-10 22:54:54
nodes: [LoadImage, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, RHMiniMaxH3VideoGen, CreateVideo, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/商品图一键变广告视频｜AI运镜带货短片（Seedance 1.5 Pro）_2093726458266079233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/商品图一键变广告视频｜AI运镜带货短片（Seedance 1.5 Pro）_2093726458266079233.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `LoadImage`
- `SaveVideo`
- `RHMiniMaxH3ModelLoader`
- `RHMiniMaxH3TextEncoderLoader`
- `RHMiniMaxH3VAELoader`
- `RHMiniMaxH3VideoGen`
- `CreateVideo`
- `CR Prompt Text`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LoadImage`、`SaveVideo`、`RHMiniMaxH3ModelLoader`、`RHMiniMaxH3TextEncoderLoader`、`RHMiniMaxH3VAELoader`、`RHMiniMaxH3VideoGen`、`CreateVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、RHMiniMaxH3TextEncoderLoader、RHMiniMaxH3VAELoader、SaveVideo、CreateVideo、RHMiniMaxH3ModelLoader、RHMiniMaxH3VideoGen、sd15-t2i-basic

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
